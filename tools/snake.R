#!/usr/bin/Rscript


setwd("~/rdata")
load("~/rdata/.RData")

# 初始化环境变量
init<-function(){
 e<<-new.env()
 e$stage<-0 #场景
 e$width<-e$height<-20  #切分格子
 e$step<-1/e$width #步长
 e$m<-matrix(rep(0,e$width*e$height),nrow=e$width)  #点矩阵
 e$dir<-e$lastd<-'up' # 移动方向
 e$head<-c(2,2) #初始蛇头
 e$lastx<-e$lasty<-2 # 初始化蛇头上一个点
 e$tail<-data.frame(x=c(),y=c())#初始蛇尾

 e$col_furit<-2 #水果颜色
 e$col_head<-4 #蛇头颜色
 e$col_tail<-8 #蛇尾颜色
 e$col_path<-0 #路颜色
}

# 获得矩阵的索引值
index<-function(col) which(e$m==col)

# 游戏中
stage1<-function(){
 e$stage<-1

 # 随机的水果点
 furit<-function(){
   if(length(index(e$col_furit))<=0){ #不存在水果
     idx<-sample(index(e$col_path),1)

     fx<-ifelse(idx%%e$width==0,10,idx%%e$width)
     fy<-ceiling(idx/e$height)
     e$m[fx,fy]<-e$col_furit

     print(paste("furit idx",idx))
     print(paste("furit axis:",fx,fy))
   }
 }


 # 检查失败
 fail<-function(){
   # head出边界
   if(length(which(e$head<1))>0 | length(which(e$head>e$width))>0){
     print("game over: Out of ledge.")
     keydown('q')
     return(TRUE)
   }

   # head碰到tail
   if(e$m[e$head[1],e$head[2]]==e$col_tail){
     print("game over: head hit tail")
     keydown('q')
     return(TRUE)
   }

   return(FALSE)
 }


 # snake head
 head<-function(){
   e$lastx<-e$head[1]
   e$lasty<-e$head[2]

   # 方向操作
   if(e$dir=='up') e$head[2]<-e$head[2]+1
   if(e$dir=='down') e$head[2]<-e$head[2]-1
   if(e$dir=='left') e$head[1]<-e$head[1]-1
   if(e$dir=='right') e$head[1]<-e$head[1]+1

 }

 # snake body
 body<-function(){
   e$m[e$lastx,e$lasty]<-0
   e$m[e$head[1],e$head[2]]<-e$col_head #snake
   if(length(index(e$col_furit))<=0){ #不存在水果
     e$tail<-rbind(e$tail,data.frame(x=e$lastx,y=e$lasty))
   }

   if(nrow(e$tail)>0) { #如果有尾巴
     e$tail<-rbind(e$tail,data.frame(x=e$lastx,y=e$lasty))
     e$m[e$tail[1,]$x,e$tail[1,]$y]<-e$col_path
     e$tail<-e$tail[-1,]
     e$m[e$lastx,e$lasty]<-e$col_tail
   }

   print(paste("snake idx",index(e$col_head)))
   print(paste("snake axis:",e$head[1],e$head[2]))
 }

 # 画布背景
 drawTable<-function(){
   plot(0,0,xlim=c(0,1),ylim=c(0,1),type='n',xaxs="i", yaxs="i")
 }

 # 根据矩阵画数据
 drawMatrix<-function(){
   idx<-which(e$m>0)
   px<- (ifelse(idx%%e$width==0,e$width,idx%%e$width)-1)/e$width+e$step/2
   py<- (ceiling(idx/e$height)-1)/e$height+e$step/2
   pxy<-data.frame(x=px,y=py,col=e$m[idx])
   points(pxy$x,pxy$y,col=pxy$col,pch=15,cex=4.4)
 }

 furit()
 head()
 if(!fail()){
   body()
   drawTable()
   drawMatrix()
 }
}

# 开机画图
stage0<-function(){
 e$stage<-0
 plot(0,0,xlim=c(0,1),ylim=c(0,1),type='n',xaxs="i", yaxs="i")
 text(0.5,0.7,label="",cex=5)
 text(0.5,0.4,label="",cex=2,col=4)
 text(0.5,0.3,label="",cex=2,col=2)
 text(0.2,0.05,label="",cex=1)
 text(0.5,0.05,label="",cex=1)
}

# 结束画图
stage2<-function(){
 e$stage<-2
 plot(0,0,xlim=c(0,1),ylim=c(0,1),type='n',xaxs="i", yaxs="i")
 text(0.5,0.7,label="Game Over",cex=5)
 text(0.5,0.4,label="Space to restart, q to quit.",cex=2,col=4)
 text(0.5,0.3,label=paste("Congratulations! You have eat",nrow(e$tail),"fruits!"),cex=2,col=2)
 text(0.2,0.05,label="Author:DanZhang",cex=1)
 text(0.5,0.05,label="http://blog.fens.me",cex=1)
}

# 键盘事件
keydown<-function(K){
 print(paste("keydown:",K,",stage:",e$stage));

 if(e$stage==0){ #开机画面
   init()
   stage1()
   return(NULL)
 }

 if(e$stage==2){ #结束画面
   if(K=="q") q()
   else if(K==' ') stage0()
   return(NULL)
 }

 if(e$stage==1){ #游戏中
   if(K == "q") {
     stage2()
   } else {
     if(tolower(K) %in% c("up","down","left","right")){
       e$lastd<-e$dir
       e$dir<-tolower(K)
       stage1()
     }
   }
 }
 return(NULL)
}

#######################################
# RUN
#######################################

run<-function(){
 par(mai=rep(0,4),oma=rep(0,4))
 e<<-new.env()
 stage0()

 # 注册事件
 getGraphicsEvent(prompt="Snake Game",onKeybd=keydown)
}

X11(type="Xlib")

run()


