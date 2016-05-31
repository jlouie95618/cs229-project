library(MASS)
library(XLConnect)


path <- "/Users/awells/Desktop/Senior_Year/SPRING_QUARTER/cs229/final_project/cs229-project/data/old_data_designation/medicare_population_demographics/TA1_demographics.xls"

wb <- loadWorkbook(path)
worksheet<- readWorksheet(wb,sheet = getSheets(wb))

data <- data.frame(worksheet)
data <- data[-c(1,2,310,311,312),]
data <- data[,-c(2,3)]

colnames(data) <- c("HRR_ID","Total Medicare Beneficiaries age 65-99",
                    "Percent of U.S. population age 75 and older (2010)",
                    "Percent of Medicare Beneficiaries whose race was non-Hispanic white",
                    "Percent of Medicare Beneficiaries whose race was black",
                    "Percent of Medicare Beneficiaries whose race was Hispanic",
                    "Percent of Medicare Beneficiaries receiving fee-for-service care",
                    "Percent of Medicare Beneficiaries living in nursing homes",
                    "Percent of Medicare beneficiaries eligible for Medicaid")

wb_out <- loadWorkbook('demographic_features.xls',create =TRUE)
createSheet(wb_out,'features')
writeWorksheet(wb_out,data,'features')
saveWorkbook(wb_out)




