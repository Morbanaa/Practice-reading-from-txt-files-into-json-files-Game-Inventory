import json

def main(): 
    try:
        inventory = []
        with open("text.txt","r") as file:
            content = file.readlines()

            item = {}
            for line in content:
                clean_line = line.strip()
                if clean_line == "":
                    continue
                elif not clean_line.count("|") == 4:
                    continue
                else:
                    val = clean_line.split("|")
                    item["Item Name:"] = val[0].strip()
                    item["Type:"] = val[1].strip()
                    item["Rarity:"] = val[2].strip()
                    item["Quantity"] = int(val[3])
                    item["Gold Value:"] = int(val[4])

                    inventory.append(item)
                    item = {}

        with open("data.json","w") as file:
            json.dump(inventory,file,indent=4)

    except FileNotFoundError:
        print("File Not Found, Check File Path")
       
           
if __name__ == "__main__":
    main()
