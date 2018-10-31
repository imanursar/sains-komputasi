library(animation)
saveGIF({
  ani.options(interval = 0.2, nmax = 5) #perframe
  
  idx = seq(1,length(tt),5) #perframe
  for (j in seq_along(idx)-1) {
    plot(tt,s,type='n',ylab = "Population",ylim = c(0,1))
    points(tt[seq(idx[j])],s[seq(idx[j])],col='green',pch=20)
    points(tt[seq(idx[j])],i[seq(idx[j])],col='blue',pch=20)
    points(tt[seq(idx[j])],r[seq(idx[j])],col='red',pch=20)
    #ani.pause()  ## pause for a while ('interval')
  }
}, interval = 0.01, movie.name = "comet_demo_.gif", 
outdir = "/usr/temp",ani.width = 600, ani.height = 600)