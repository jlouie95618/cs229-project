library(MASS)
library(XLConnect)

path <- '/Users/awells/Desktop/Senior_Year/SPRING_QUARTER/cs229/final_project/cs229-project/data/old_data_designation/hospital_level_data/DAP_hospital_data_2012.xls'

wb <- loadWorkbook(path)
worksheets <- readWorksheet(wb,sheet = getSheets(wb))

data <- data.frame(worksheets)
data <- data.frame(data[-c(1,2),])
data <- data.frame(data[,-c(1,2,4,5,6,7,30,32,38,40)])
labels <- data.frame(data[,c(5)])
data <- data.frame(data[,-c(5)])

wb_out <- loadWorkbook('dap_data.xls',create =TRUE)
createSheet(wb_out,'dap_data')
writeWorksheet(wb_out,data,'dap_data')
saveWorkbook(wb_out)

wb_out2 <- loadWorkbook('dap_labels.xls',create =TRUE)
createSheet(wb_out2,'dap_labels')
writeWorksheet(wb_out2,labels,'dap_labels')
saveWorkbook(wb_out2)