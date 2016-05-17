library(MASS)
library(XLConnect)

path <- "/Users/awells/Desktop/Senior_Year/SPRING_QUARTER/cs229/final_project/cs229-project/data/hrr_level_data/"
hrr_filenames <- c("post_discharge_events_hrr_11.xls","PC_HRR_rates_2011.xls","pa_reimb_hrr_2011.xls","DAP_hrr_data_2011.xls","2011_phys_hrr.xls")
all_files <- list()


parse_post_discharge<-function(worksheets){
  pd_df <- data.frame()
  c2 <- c(4,5,8,11,14)
  c3 <- c(4,5,8,11)
  c_n <- c(4,5,8,11,14)
  for(t in 1:length(worksheets)){ #loop over tabs
    if(t==1){ #skip first tab
      next
    }
    if(t==2){ #medical cohort
      df <- data.frame(worksheets[t])
      df <- df[,c2]
      pd_df <- df
    } else if(t==3) {
      df <- data.frame(worksheets[t])
      df <- df[,c3]
      df[is.na(df)] <- 0
      pd_df <- cbind(pd_df,df)
    } else if(t>3){
      df <- data.frame(worksheets[t])
      df <- df[,c_n]
      df[is.na(df)] <- 0
      pd_df <- cbind(pd_df,df)
    }
  }
  return(pd_df)
}

parse_pc<-function(worksheets){
  cols <- c(3,6,15,18,27,36,45,48,57,60,69)
  pc_df <- data.frame(worksheets)
  pc_df <- pc_df[,cols]
  return(pc_df)
}

parse_reimb <- function(worksheets){
  cols <- c(6)
  r_df <- data.frame(worksheets)
  r_df <- r_df[,cols]
  return(r_df)
}

parse_phys<-function(worksheets){
  cols <- c(1)
  cols2 <- (4:length(worksheets[1,]))
  c_n <- c(cols,cols2)
  p_df <- data.frame(worksheets)
  p_df <- p_df[,c_n]
  return(p_df)
}


for(f in 1:length(hrr_filenames)){
  f_tot <- paste(path,hrr_filenames[f],sep = '')
  wb <- loadWorkbook(f_tot)
  worksheets <- readWorksheet(wb,sheet = getSheets(wb))
  if(f==1){
    pd_df <- parse_post_discharge(worksheets)
    pd_df <- pd_df[2:length(pd_df[,1]),]
  } else if(f==2){
    pc_df <- parse_pc(worksheets)
    pc_df <- pc_df[3:length(pc_df[,1]),]
  } else if(f==3){
    r_df <- parse_reimb(worksheets)
  } else if(f == 5){
    p_df <- parse_phys(worksheets)
  }
}
total_df <- cbind(p_df,pc_df,pd_df)

wb_out <- loadWorkbook("hrr_data_total.xls",create = TRUE)
createSheet(wb_out,"hrr_dat")
writeWorksheet(wb_out,total_df,"hrr_dat")
saveWorkbook(wb_out)