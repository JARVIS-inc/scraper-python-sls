# Serveless Python Selenium Lambdas (in future possibly API)
This project is about creating aws lambdas to scrape and take screenshots of stuff and uploading said screenshots to S3
The idea is that this service could be used in unison with a alexa skill to create visual alexa skills for whatever

## Local development
`make docker-build` - Creating a docker image for offline execution 

`docker-compose run lambda <HANDLER>.<FUNCTION> "$(cat <INPUTMESSAGEJSONFILE>)"` - executing lambdas
e.g.
`docker-compose run lambda handler.scrapeshot "$(cat event.json)"`

### Local development limitations. 
For some reason the docker will not automatically get environment variables from serverless.yml 
This is a TODO but for know they are manually entered to the docker-compose.

## Deployment
This project requires serverles framework

`make lambda-layer-build` creating the lambda layer zip file (only needed if binaries are changed)

`sls deploy`Deploy through serverless (check serverless.yml for details)

## Binaries and help 

The binaries and inspiration came from https://levelup.gitconnected.com/chromium-and-selenium-in-aws-lambda-6e7476a03d80

If making new zip files of binaries on MAC OSX you need to run the following command to remove __MAXOSX entries (mac...)

`zip -d bin.zip "__MACOSX*"`




