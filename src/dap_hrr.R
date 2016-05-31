library(MASS)
library(XLConnect)


path <- "/Users/awells/Desktop/Senior_Year/SPRING_QUARTER/cs229/final_project/cs229-project/data/old_data_designation/hrr_level_data"
names <- c("DAP_hrr_data_2010.xls","DAP_hrr_data_2011.xls","DAP_hrr_data_2012.xls","DAP_hrr_data_2013.xls")

paths <- c()
for(name in names){
  paths <- c(paths, paste(path,name))
}

for(file in paths){
  wb <- loadWorkbook(file)
  worksheets <- readWorksheet(wb,sheet = getSheets(wb))
}
  