class Configuration:
    """
    Define the credentials needed to establish a connection with twitter and do streaming.
    https://apps.twitter.com/
    """

    def __init__(self):
        self.Version = 0.1
        self.Author = 'CAOBA_Extraccion'

    def MONGO_URL(self):
        """

        :rtype: String
        :returns:mongodb server direction
        """

        return 'mongodb://localhost:27017//'

    ##        return 'mongodb://10.2.2.133:27017//'

    def MONGO_DB(self):
        """

        :rtype: String
        :returns:String: name of the data base to be created on mongo
        """
        return 'local'

    def MONGO_COLL1(self):
        """

        :rtype: String
        :returns:name of the collection where the Twitter data will be saved
        """
        return 'tweetsGNIP24'