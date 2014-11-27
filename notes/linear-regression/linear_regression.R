#!/usr/bin/Rscript

get_gradient <- function(x,y,theta0,theta1) {
    m = length(x)
    s = matrix(0,2,1)
    for (i in 1:m) {
        s[1,1] = s[1,1] + theta0 + theta1 * x[i] - y[i]
        s[2,1] = s[2,1] + (theta0 + theta1 * x[i] - y[i]) * x[i]
    }
    return(1/m*s)
}

J <- function(x,y,theta0,theta1){
    m = length(x)
    s = 0
    for (i in 1:m){
        s = s + (theta0 + theta1 * x[i] - y[i])^2
    }
    return(1/(2*m)*s)
}

x = c(round(runif(15,min=50,max=105)))
noise <- rnorm(15,0,20)
y = c(round(4.5*x + 5 + noise))
#x = c(95,68,79,69,93,63,75,101,92,57,105,89,74,78,71)
#y = c(389,323,340,295,388,234,355,461,397,269,452,393,358,338,302)
print(x) #显示样本集-面积
print(y) #显示样本集-售价
alpha = 0.0001  #这个值相对较合适。尝试了多个值，更大的alpha可能会使J过大而不收敛，更小的alpha可能收敛过慢
theta = matrix(1, 2, 1)
for (i in 1:100) {
    gradient = get_gradient(x,y,theta[1,1],theta[2,1])
    theta = theta - alpha * gradient
}
print(theta) #打印参数结果
print(J(x,y,theta[1,1],theta[2,1])) #打印cost funciton的值，可以从该值看出是否收敛

xx <- 40:120
yy <- theta[1,1]+theta[2,1]*xx

#画图，将散点图和回归直线画在一起
plot(x,y,xlab='size',ylab='cost',xlim=c(40,130),ylim=c(150,550))
par(new=TRUE)
plot(xx,yy,type="l",col="blue",xlab='',ylab='',xlim=c(40,130),ylim=c(150,550))

