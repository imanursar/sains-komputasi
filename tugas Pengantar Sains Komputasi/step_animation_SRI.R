library(animation)
saveGIF({
  ani.options(interval = 0.2, nmax = 20) #perframe
  
  idx = seq(1,length(ti),20) #perframe
  for (i in seq_along(idx)) {
    plot(ti,p,type='n',ylab = "Population")
    points(ti[seq(idx[i])],p[seq(idx[i])],col='red',pch=20)
    #ani.pause()  ## pause for a while ('interval')
  }
}, interval = 0.01, movie.name = "comet_demo_.gif", 
outdir = "/usr/temp",ani.width = 600, ani.height = 600)