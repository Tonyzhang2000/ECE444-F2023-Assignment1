class Utils:

    def reversed(num):

        # Check if int
        if not isinstance(num, int):
            raise TypeError("Input must be an integer")
        else:
            # Get the sign of the number
            sign = -1 if num < 0 else 1

            # Force number positive
            num = abs(num)

            # Reverse the number
            rev = 0
            while num > 0:
                rev = (10 * rev) + num % 10
                num //= 10
        
        return sign * rev
    
    def formatter(num):

        # Check if int
        if not isinstance(num, int):
            raise TypeError("Input must be an integer")
        
        # Chenge the number to binary format
        binary = bin(num)

        # Change the number to octal format
        octal = oct(num)

        return binary, octal
        
        
    
# Check if the file is being run directly
if __name__ == "__main__":

    # Run the reversed function
    print(Utils.reversed(123))

    # Run the formatter function
    print(Utils.formatter(10))