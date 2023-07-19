# Carbon Samples - La Jara Creek #
#### This repo is meant to hold all data for POC and DOC samples I will be running in the mass spec with the help of Korvin Jones / Summer 2023 field season ####

## Things to do: 
- [x] Compensate all stilling well pressure data and convert to water depths - *Nicole*.
- [x] Separate all piezometer files by field seasons, leaving one large hydrograph by season - *Korvin*.
      
      These field seasons should be:  - Summer 2021 (July to August)
                                      - Spring 2022 (March to May)
                                      - Summer 2022 (July to August)
                                      - Spring 2023 (March to May)
      
      There should be 4 files for each piezometer, and they should be named as: P#_fieldseason. For example: P4_spring2022
      Please use the files from the COMPENSATED FLOW DEPTH folder
      This does not include the summer 2022 experiments, those will have their own seperate hydrographs 
      Note: The exact dates of each season will vary, so please note the exact date each season starts and finishes
      
- [ ] Plot all water depths of all the piezometers together **for each season** - *Korvin*.

      This is to see if there are any considerable time lags between peaks.
      Feel free to use whatever software that works best for you to do this!
      
- [x] Write down ALL samples we have stored for POC and sort by chronological order. - *Korvin (Nicole will help with sample date and time)*. 

      Some samples will not have any dates on them. For this we will look into field notebooks from previous seasons.
      The end product of this step should be a CSV file with all the samples ID and date in chronollogical order.
      
      | Sample number |   Sample ID   |    Date and time    |
      | ------------- | ------------- | ------------------- |
      | # (in order)  |  NAME ON BAG  | MM/dd/yyyy hh:mm:ss |

- [ ] Plot the samples POC alongside the hydrograph of **EACH piezometer**. - *Korvin*.

      Each plot should look something like the following image, where each red dot corresponds to a sample.
      If possible, displaying the samples number (not ID) would be really beneficial for sample selection.

    <img src="https://cdn.discordapp.com/attachments/696204356650926092/1126929323597770933/image.png" alt="Alt Text" width="400" height="150">

- [ ] Repeat sample organization for DOC samples and create the same plots as above for DOC. - *Nicole and Korvin*

- [ ] Once all this is done, plan out to do the same with all summer 2022 experiment samples. - *Korvin*.


## Notes: 
- All piezometer data has a data gap from sprind 2022 to summer 2022 due to a wildfire, so we took all of them out of the stream just in case.
- P5 has negative depths, I will revisit this once done. For now, we can skip it. 
- P3 has 3 different files. Same as the wildfires, but there was also a malfunction during spring of 2023 (all those constant 14's), so the diver got replaced.
  *Please note the date it stopped working.*
- P1 during the summer of 2022 has a small gap as well, since this is the pressure transducer we used for the flow experiments (we just changed the name).
- I have both compensated and uncompensated data in different folders in case you wanted to see the code that is able to do this. 

## Appendix: 
Table 1. Pressure transducer depths before and after they were re-installed. This is important info when compensating for them.
| Diver ID    | Depth Summer 2021 to Spring 2022 (cm) | Depth Summer 2022 to Present (cm) |
| :---------: | :-----------------------------------: | :-------------------------------: |
| P1 - A      |                69.6                   |              74.6                 |
| P1 - B      |                52.5                   |              51.4                 |
| P1 - C      |                37.3                   |              39.8                 |
| P2 - A      |                52.6                   |              69.0                 |
| P2 - B      |                49.0                   |              57.5                 |
| P2 - C      |                39.3                   |              42.8                 |
| P3 - A      |                60.4                   |              61.6                 |
| P3 - B      |                55.7                   |              56.2                 |
| P3 - C      |                38.0                   |              29.3                 |
| P4 - A      |                67.0                   |              65.6                 |
| P4 - B      |                51.4                   |              56.0                 |
| P4 - C      |                39.7                   |              38.4                 |
| P5 - A      |                71.1                   |              72.4                 |
| P5 - B      |                53.2                   |              58.6                 |
| P5 - C      |                38.3                   |              47.7                 |
| P6 - A      |                64.3                   |              70.5                 |
| P6 - B      |                55.1                   |              57.4                 |
| P6 - C      |                39.3                   |              40.0                 |
| GW1         |                101.6                  |              97.0                 |
| GW2         |                89.0                   |              104.0                |
| GW3         |                110.7                  |              104.0                |
| GW4         |                112.2                  |              107.0                |
| GW5         |                106.1                  |              104.4                |
| GW6         |                107.1                  |              105.4                |
| GW7         |                108.8                  |              104.5                |
| GW8         |                113.8                  |              100.5                |
| GW9         |                92.1                   |              98.8                 |
