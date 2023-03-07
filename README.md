# R-extension: A LOKO AI tools to write code in R within the platform

This extension provide a component that allows to write and run R code within the software. It's very easy to use, you just need to write code inside the block and link a Trigger component to the R input. Clicking on the Trigger's play button, the code will be runned.


# :wrench: Configuration


To configure and adapt this extension to your preference you can set inside the config.json file the local path of the volume that the container will use. You can put there all the file you may want to read using directly the R components or either way save in that path some files. 


The default path is ```"/var/opt/loko/projects/r/data"```.


An other configuration you may want to adapt to your needs is the default set of packages that will automatically be installed when building the extensions. Specifically, it's possibile to add or remove packages modifying the ```"r_requirements.txt"``` file. 

If you have already installed this extension, you can find these files inside the _loko_ folder, such as: ```"/home/$USER/loko/shared/extensions/r-extension/"```


# :mag_right: How to use it?

Here some tips that could help in case you want to read a file, save a file, or maybe a plot: 

- **Read a file:** to read a file use the command that suits your data type, and as path use this root ```/plugin/data/```. In the example below, we are reading a csv file named _"data.csv"_ which we stored in the path ```"/var/opt/loko/projects/r/data"``` and will be available in the volume of the container to the path ```/plugin/data/```, as we declared in the _config.json_ file.
    ``` r
    data <- read.csv(file = '/plugin/data/data.csv')
    ```
- **Write a file:** as seen for the reading, to write a file we need to point to the ```/plugin/data/``` path. For example, you may want to save a plot, using the R sintax and setting the file name, as showed in the following code section, when running the flow in Loko AI, you will generate in the ```"/var/opt/loko/projects/r/data"``` path the file *"corr_plot.pdf"*.
    ``` r
    # compute correlation matrix
    corr <- round(cor(data), 1)
    # correlation plot
    corr_plot <- ggcorrplot(corr,
               type = "lower",
               lab = TRUE, 
               lab_size = 6,  
               colors = c("tomato", "blue", "springgreen3"),
               title="Correlogram of Example Dataset", 
               ggtheme=theme_bw)
    #save the file
    pdf("/plugin/data/corr_plot.pdf")
    print(corr_plot)
    dev.off()
    ```