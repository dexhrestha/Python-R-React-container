# Loading package
library(plumber)

# Routing API
r <- plumb("api.r")

# Running API
r$run(port = 8000,host="0.0.0.0")
