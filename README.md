# song-search-engine

The project is aim to develop a search engine to get more information for Kelivi keyword search system.

## Build
```
docker build --platform linux/amd64 -t keyword-search-engine:latest
```

## Run
```
docker run --name my-keyword-search-engine -dp 5000:5000 keyword-search-engine
```

## Monitor
```
docker logs -f my-keyword-search-engine
```