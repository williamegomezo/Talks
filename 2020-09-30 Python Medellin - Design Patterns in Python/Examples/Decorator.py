class DataSource:
    def writeData(self, data):
        print(f'data is being written: {data}')

    def readData(self, data):
        print(f'data is being read: {data}')


class EncryptionDecorator():
    def __init__(self, wrappee):
        self.wrappee = wrappee

    def writeData(self, data):
        # 1. Encrypt passed data.
        encrypted_data = f'${data}$'
        # 2. Pass encrypted data to the wrappee's writeData
        # method.
        self.wrappee.writeData(encrypted_data)

    def readData(self, data):
        # 1. Get data from the wrappee's readData method.
        # 2. Try to decrypt it if it's compressed.
        decrypted_data = f'_${data}$_'
        # 3. Return the result.
        self.wrappee.readData(decrypted_data)

# You can wrap objects in several layers of decorators.


class CompressionDecorator:
    def __init__(self, wrappee):
        self.wrappee = wrappee

    def writeData(self, data):
        # 1. Compress passed data.
        compressed_data = f'[{data}]'
        # 2. Pass compressed data to the wrappee's writeData
        # method.
        self.wrappee.writeData(compressed_data)

    def readData(self, data):
        # 1. Get data from the wrappee's readData method.
        # 2. Try to decompress it if it's compressed.
        # 3. Return the result.
        decompressed_data = f'_[{data}]_'
        self.wrappee.readData(decompressed_data)


compression_data_source = CompressionDecorator(DataSource())
compression_data_source.writeData('Data')
compression_data_source.readData('Data')

encryption_data_source = EncryptionDecorator(DataSource())
encryption_data_source.writeData('Data')
encryption_data_source.readData('Data')

both_data_source = CompressionDecorator(EncryptionDecorator(DataSource()))
both_data_source.writeData('Data')
both_data_source.readData('Data')