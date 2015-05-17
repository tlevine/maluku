voyages.raw <- read.csv('voyages.csv', stringsAsFactors = FALSE)
voyages <- voyages.raw['Number']
names(voyages) <- 'number'

d <- function(x) strptime(x, '%d-%m-%Y')

voyages$ship <- factor(voyages.raw$Name.of.ship)
voyages$master <- factor(voyages.raw$Master)
voyages$tonnage <- as.numeric(sapply(strsplit(voyages.raw$Tonnage, '/'),
                                     function(x) if (length(x) > 0) x[length(x)] else NA))
voyages$ship.type <- factor(voyages.raw$Type.of.ship)
voyages$built <- as.numeric(voyages.raw$Built)
voyages$yard <- as.numeric(voyages.raw$Yard)
voyages$chamber <- as.numeric(voyages.raw$Chamber)
voyages$departure.date <- d(voyages.raw$Date.of.departure)
voyages$departure.place <- factor(voyages.raw$Place.of.departure)
voyages$cape.arrival.date <- d(voyages.raw$Arrival.at.Cape)
voyages$cape.departure.date <- d(voyages.raw$Departure.from.Cape)
voyages$arrival.date <- d(voyages.raw$Date.of.arrival.at.destination)
voyages$destination.chamber <- factor(voyages.raw$Chamber.for.which.cargo.is.destined)
voyages$particulars <- voyages.raw$Particulars
voyages$onbcategory <- factor(voyages.raw$onbcategory)
voyages$I <- as.numeric(voyages.raw$I)
voyages$II <- as.numeric(voyages.raw$II)
voyages$III <- as.numeric(voyages.raw$III)
voyages$IV <- as.numeric(voyages.raw$IV)
voyages$V <- as.numeric(voyages.raw$V)
