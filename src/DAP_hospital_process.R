library(MASS)
library(XLConnect)

path1 <- '/Users/awells/Desktop/Senior_Year/SPRING_QUARTER/cs229/final_project/cs229-project/data/old_data_designation/hospital_level_data/DAP_hospital_data_2010.xls'
path2 <- '/Users/awells/Desktop/Senior_Year/SPRING_QUARTER/cs229/final_project/cs229-project/data/old_data_designation/hospital_level_data/DAP_hospital_data_2011.xls'
path3 <- '/Users/awells/Desktop/Senior_Year/SPRING_QUARTER/cs229/final_project/cs229-project/data/old_data_designation/hospital_level_data/DAP_hospital_data_2012.xls'
path4 <- '/Users/awells/Desktop/Senior_Year/SPRING_QUARTER/cs229/final_project/cs229-project/data/old_data_designation/hospital_level_data/DAP_hospital_data_2013.xls'
paths <- c(path1,path2,path3,path4)

data_total <- data.frame()
labels <- data.frame()
count <- 0
for(path in paths){
  wb <- loadWorkbook(path)
  worksheets <- readWorksheet(wb,sheet = getSheets(wb))
  
  data <- data.frame(worksheets)
  names <- data.frame(data[1,])
  data <- data.frame(data[-c(1,2),])
  data <- data.frame(data[,-c(1,2,4,5,6,7,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,38,40)])
  names <- data.frame(names[,-c(1,2,4,5,6,7,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,38,40)])
  #lab <- data.frame(data$Table.5..The.Medical.Care.Cost.Equation..Disaggregation.of.payments.for.physician.visits.per.decedent.into.contributions.of.volume..physician.visits.per.decedent..and.price..average.payments.per.physician.visit..during.the.last.two.years.of.life..deaths.occurring.in.2012.)
  lab <- data.frame(data[,c(5)])
  data <- data.frame(data[,-c(5)])
  colnames(data) <- sprintf("col%s",seq(1:40))
  if(count == 0){
    data_total <- data
    labels <- lab
  } else {
    data_total <- rbind(data_total,data)
    labels <- rbind(labels,lab)
  }
  count <- count + 1
}

#wb_out <- loadWorkbook('dap_hd.xls',create =TRUE)
#createSheet(wb_out,'dap_hd')
#writeWorksheet(wb_out,data_total,'dap_hd')
#saveWorkbook(wb_out)

#wb_out2 <- loadWorkbook('dap_hd_labels.xls',create =TRUE)
#createSheet(wb_out2,'dap_hd_labels')
#writeWorksheet(wb_out2,labels,'dap_hd_labels')
#saveWorkbook(wb_out2)

#wb_out3 <- loadWorkbook('dap_features.xls',create =TRUE)
#createSheet(wb_out3,'dap_hd_features')
#writeWorksheet(wb_out3,names,'dap_hd_features')
#saveWorkbook(wb_out3)


