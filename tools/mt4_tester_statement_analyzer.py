#!/usr/bin/env  python


import re
import hashlib
import sys,getopt
import psycopg2,psycopg2.extras


from lxml import etree

#from lxml.html import parse
#page = parse("./GBPNZD.htm")


def main(argv):
    inputfile = ''
    htmlpage  = ''
    htmltree  = ''
    conn_str  = "host='' dbname='postgres' user='postgres'"

    try:
        opts, args = getopt.getopt(argv,"hf:",["file="])
    except getopt.GetoptError:
      print 'mt4_tester_statement_analyzer.py -f <file>'
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'mt4_tester_statement_analyzer.py -f <file>'
            sys.exit()
        elif opt in ("-f", "--file"):
            inputfile = arg

    try:
        htmlpage = open(inputfile).read()
    except:
        print 'Open file: <%s> failed' % inputfile
        sys.exit(2)


    htmltree = etree.HTML(htmlpage)
    s = parse_summary(htmltree)
    r = parse_record(htmltree)

    p = dict(re.findall(r'(\S+?)=(".+?"|[^;]);', s['Parameters']))

    conn = psycopg2.connect(conn_str)
    t = pgdb_create_table(conn,s)
    pgdb_insert_table(conn,t,s,p,r)


# create table via summary (s)
def pgdb_create_table(conn,s):
    comment = "%s|%s|%s|%s" % (s['Symbol'], s['Period'] ,s['htmltitle'], s['Model'] )
    tblname = hashlib.md5(comment).hexdigest()

    create_table_str = """
    create table str.t_%s (id SERIAL, h hstore);
    """ % (tblname)

    comment_table_str = """
    comment on table str.t_%s is '%s'
    """ % (tblname,comment)

    cursor = conn.cursor()
    cursor.execute(create_table_str)
    cursor.execute(comment_table_str)
    conn.commit()
    cursor.close()

    return tblname

# insert into table s,p,r
# s for summary dict
# p for parameter dict
# r for record(table2) dict
def pgdb_insert_table(conn,tblname,s,p,r):

    cursor = conn.cursor()

    del s['Parameters']

    s_items = ','.join(
        ["\"{key}\"=>\"{value}\"".format(key=k, value=v) for (k,v) in s.iteritems()])

    p_items = ','.join(
        ["\"{key}\"=>{value}".format(key=k, value=v) for (k,v) in p.iteritems()])


    insert_str_s = """
    insert into str.t_%s( h ) values ( '%s'::public.hstore );
    """ % (tblname,s_items)

    insert_str_p = """
    insert into str.t_%s( h ) values ( '%s'::public.hstore );
    """ % (tblname,p_items)


    cursor.execute(insert_str_s)
    cursor.execute(insert_str_p)

    head_idx = list()

    for idx in r:
        if idx[0] == '#':
            idx[0] = 'n'
            head_idx = idx
            continue

        r_items = ','.join(
            ["\"{key}\"=>\"{value}\"".format(key=k, value=v) for (k,v) in zip(head_idx,idx)])

        insert_str_r = """
        insert into str.t_%s( h ) values ( '%s'::public.hstore );
        """ % (tblname, r_items)

        cursor.execute(insert_str_r)

    conn.commit()
    cursor.close()

    return

def parse_summary(html):
    s    = dict()
    prev = ''

    for i in html.xpath('//table[1]//td'):

        if i.text is None or i.text == 'Largest' or i.text == 'Average' or i.text == 'Maximum' or i.text == 'Maximal':
            continue

        if not s.has_key(prev):
            prev = i.text.strip()
            s[prev] = ''
        else:
            s[prev] = i.text.strip()
            prev = ''

    #  for table name 
    s['htmltitle'] = html.xpath("/html/head/title")[0].text.strip().replace("Strategy Tester: ","")

    return s


def parse_record(html):

    rows = html.xpath("//table")[1].findall("tr")
    data = list()

    for row in rows:
        data.append([c.text for c in row.getchildren()])

    return data


if __name__ == "__main__":
    main(sys.argv[1:])
