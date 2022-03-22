def get_links(FileWay):
    try:
        with open(FileWay, "r") as File:
            ArrayOfLinks = []
            for link in File:
                link = link[:link.find('/n')]
                ArrayOfLinks.append(link)

            return ArrayOfLinks

    except:
        print("File reading error")
