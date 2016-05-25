from xml.dom.minidom import parse, parseString


def parseXML(file):
    data = parse(file)
    chains = data.getElementsByTagName("CHAIN")
    alphaSequences = []
    for chain in chains:
        if chain.getAttribute("TYPE") == "alpha":
            sequence = chain.getElementsByTagName("SEQ")[0].firstChild.nodeValue.replace(" ", "").replace("\n", "")
            regions = chain.getElementsByTagName("REGION")
            for region in regions:
                if region.getAttribute("type") == "H":
                    start = int(region.getAttribute("seq_beg"))
                    end = int(region.getAttribute("seq_end"))
                    alphaSequences.append(sequence[start-5:end+5])
    return alphaSequences


if __name__ == "__main__":
    print(parseXML('pdbtmall.xml'))
