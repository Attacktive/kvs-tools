class ArchiveType:
    """Group the file signature and its extension."""

    def __init__(self, signature, extension):
        """
        Initialize a new :class:`ArchiveType` instance.

        It's NOT meant to be invoked outside since I actually wanted something like Java enums.

        :param bytes signature: The file signature (the magic bytes)
        :param str extension: The file extension INCLUDING the leading dot (.)
        :rtype: ArchiveType
        """
        self.signature = signature
        self.extension = extension


ArchiveType.KOVS = ArchiveType(b"KOVS", ".kvs")
ArchiveType.KTSS = ArchiveType(b"KTSS", ".kns")
