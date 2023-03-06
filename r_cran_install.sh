while read -r line; do apt-get install r-cran-$line -y; done < "/r_requirements.txt"
