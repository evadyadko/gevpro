from xml.etree import ElementTree as ET


def get_adjectives(database_path):
    tree = ET.parse(database_path)
    root = tree.getroot()
    adj_set = set([cid.attrib['form'] for cid in root
                   if 'ADJ' in cid.attrib['pos']])
    return adj_set


def main():
    print(get_adjectives('cdb-sample.xml'))


if __name__ == "__main__":
    main()
