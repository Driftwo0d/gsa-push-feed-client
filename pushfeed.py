import getopt
import requests
import sys


def usage():
    print("""Usage: %s ARGS
  --datasource:  name of the datasource
  --feedtype:  full or incremental or metadata-and-url
  --url:  xmlfeed url of the feedergate, e.g. http://gsabox:19900/xmlfeed
  --xmlfilename:  The feed xml file you want to feed
  --help: output this message""" % sys.argv[0])


def main(argv):
    """
    Process command line arguments and send feed to the webserver
    """
    try:

        opts, args = getopt.getopt(argv[1:], None, ["help", "datasource=", "feedtype=", "url=", "xmlfilename="])

    except getopt.GetoptError:
        # print help information and exit:
        usage()
        sys.exit(2)

    url = None
    datasource = None
    feedtype = None
    xmlfilename = None

    for opt, arg in opts:
        if opt == "--help":
            usage()
            sys.exit()
        if opt == "--datasource":
            datasource = arg
        if opt == "--encoding":
            encoding = arg
        if opt == "--feedtype":
            feedtype = arg
        if opt == "--url":
            url = arg
        if opt == "--xmlfilename":
            xmlfilename = arg

    if url and xmlfilename and datasource and feedtype in ("full", "incremental", "metadata-and-url"):

        data = {"feedtype": feedtype, "datasource": datasource}
        files = {"data": open(xmlfilename, "rb")}

        response = requests.post(url, data=data, files=files)

        print(str(response.status_code))

    else:
        usage()
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
