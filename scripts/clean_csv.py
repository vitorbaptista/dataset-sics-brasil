import sys
import csv
import unicodedata


def strip_accents(s):
   return ''.join([
       c for c in unicodedata.normalize('NFD', s)
       if unicodedata.category(c) != 'Mn'
   ])


def clean_str(s):
    return strip_accents(s).replace(' ', '_').lower()


def main(path):
    with open(path, newline='', encoding='windows-1252') as csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(sys.stdout)

        headers = next(reader)
        clean_headers = [clean_str(header) for header in headers]
        writer.writerow(clean_headers)

        for row in reader:
            clean_row = [cell.strip() for cell in row]
            writer.writerow(clean_row)


if __name__ == '__main__':
    file_path = sys.argv[1]
    main(file_path)
