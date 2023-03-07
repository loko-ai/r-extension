# R-extension: A LOKO AI tools to write code in R within the platform

This extension provide a component that allows to write and run R code within the software. It's very easy to use, you just need to write code inside the block and link a Trigger component to the R input. Clicking on the Trigger's play button, the code will be runned.


# :wrench: Configuration


To configure and adapt this extension to your preference you can set inside the config.json file the local path of the volume that the container will use. You can put there all the file you may want to read using directly the R components or either way save in that path some files. 


The default path is ```"/var/opt/loko/projects/r/data"```.


An other configuration you may want to adapt to your needs is the default set of packages that will automatically be installed when building the extensions. Specifically, it's possibile to add or remove packages modifying the ```"r_requirements.txt"``` file. 

If you have already installed this extension, you can find these files inside the _loko_ folder, such as: ```"/home/$USER/loko/shared/extensions/r-extension/"```
