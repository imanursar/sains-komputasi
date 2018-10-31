library(animation)
saveGIF({
  ani.options(interval = 0.2, nmax = 10) #perframe
  
  idx = seq(1,length(r),10) #perframe
  for (i in seq_along(idx)) {
    plot(r,T,type='n',ylab = "Population")
    points(r[seq(idx[i])],T[seq(idx[i])],col='red',type='l')
    #ani.pause()  ## pause for a while ('interval')
  }
}, interval = 0.1, movie.name = "comet_demo_.gif", 
outdir = "/usr/temp",ani.width = 600, ani.height = 600)