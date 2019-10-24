install.packages('oro.dicom')
library(oro.dicom)

#dcmImages <- readDICOM("/home/ef2p/Kaggle/cardiac/PreTx_12_08_2016", verbose = TRUE,
#                       recursive = FALSE, exclude = "sql")
dcmImages <- readDICOM("/home/ef2p/Kaggle/cardiac/PostTx_3_17_2017", verbose = TRUE,
                       recursive = FALSE, exclude = "sql")

print(dcm.info <- dicomTable(dcmImages$hdr))
#print(length(names(dcm.info)))

for (i in 1:157) {
jpeg(paste0("/home/ef2p/Kaggle/cardiac/post-jpg/post",i,".jpg"))
i1 <- image(t(dcmImages$img[[i]]), col = grey(0:255/255), axes = FALSE,
      xlab = "x", ylab = "y")
dev.off()
#print(i)
}

# view jpeg with build-in Linux eog
