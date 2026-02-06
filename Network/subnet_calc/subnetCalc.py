"""
    Description: A tool for calculating network address, broadcast address,
    usable host ranges, and subnet mask. This assumes CIDR notation is given.

    Input: None (This could be changed to accept script arguments for providing
    a text file filled with addresses)

    Output: None (This could be changed to output a CSV or TXT file if provided
    a text file filled with addresses)
"""

## IMPORTS
import ipaddress

## CONSTANTS
menuMsg = (
        "\nPlease choose the following options:"
        "\n1. Address with CIDR notation (e.g. 10.234.23.2/17)"
        "\n2. Address with subnet mask (e.g. 10.234.23.2 255.255.128.0)"
        "\n3. Exit program\n"
    )


## HELPER FUNCTIONS
def isValidCidr(cidrInput):
    try:
        cleanInput = cidrInput.replace(" ", "")
        networkOutput = ipaddress.ip_network(cleanInput, strict=False)
        return networkOutput
    except ValueError:
        return
        
def isValidWithMask(maskInput):
    try:
        cleanInput = maskInput.strip()
        tupleInput = tuple(cleanInput.split(' '))
        networkOutput = ipaddress.ip_network(tupleInput, strict=False)
        return networkOutput
    except ValueError:
        return
        
def netObjOutput(networkObj):
    netAddr = str(networkObj.network_address)
    broadAddr = str(networkObj.broadcast_address)
    if networkObj.num_addresses > 2:
        firstHost = networkObj[1]
        lastHost = networkObj[-2]
    else:
        firstHost = 'N/A'
        lastHost = 'N/A'
    print(
        f'\nNetwork Address: {netAddr}'
        f'\nBroadcast Address: {broadAddr}'
        f'\nHost range: {firstHost} - {lastHost}\n'
    )
           
## MAIN
if __name__ == "__main__":

    ## Main Menu Message
    mainLoop = True
    while mainLoop:
        print(menuMsg)
        choice = int(input("Input: "))
        match choice:
            case 1:
                print("Please enter the address in CIDR format: ")
                cidrInput = input()
                networkObj = isValidCidr(cidrInput)
                if networkObj:
                    netObjOutput(networkObj)
                else:
                    print("Incorrect CIDR format; please try again.\n")
            case 2:
                print("Please enter the address with mask, space included: ")
                maskInput = input()
                networkObj = isValidWithMask(maskInput)
                if networkObj:
                    netObjOutput(networkObj)
                else:
                    print("Incorrect format; please try again.\n")
            case 3:
                mainLoop = False
            case _:
                print("Invalid; please choose from the given options.\n")
        
