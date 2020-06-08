# Storing Amazon product review data and processing it.

This repository downloads data from https://s3.amazonaws.com/amazon-reviews-pds
converts it from TSV to json and loads json file into mongodb.
It also aggregates the data loaded in mongodb and stores the aggregated records
in mysql.

The size of amazon review file is approximatley 2G. Storing the file into RDMS
(mysql, sql server) would take long time. The best approach would be to store in
some NoSQL database, where the loading and reading both would be fast and easy.

Mongodb is a good choice, becuase it is a document database and files can be stored
just by importing json file.

Aggregartion can be done and the results can be stored in mysql.

I tried to load the data from TSV -> JSON -> mysql using mysql insert statement
using cursor. The result was terribly slow.

The list of the files to be procesed is available in the config/tcon.json file.
Attribute "filenames" is a list - which consists of the files to be downloaded from s3 
bucket and processes. 


### Prerequisites

```
python3.6
MongoDB shell version v3.6.3
docker

```

### STEP 1 :  Build mongodb docker images to test. 
Run below commands in sequence. This will install a mongodb images and run it in background.

```
$cd monogodb
$sh build.sh
$sh run.sh
 
```

### STEP 2 :  Execute the application to fetch the file and process it.
Run below commands in sequence. This will process the files listed in config/tcon.json "filenames".

```
$sudo sh amz-review-test.sh 
 
```


## Authors

* **Abhishek Kumar** - *Initial work* - [aktechthoughts](https://github.com/aktechthoughts)


## License

This project is licensed under the MIT License.

## Acknowledgments

* **Abhishek Kumar** - *Sample * - [anisble-cheat-sheet](https://www.digitalocean.com/community/cheatsheets/how-to-use-ansible-cheat-sheet-guide)
