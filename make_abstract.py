import argparse
import os

parser = argparse.ArgumentParser(description='Text abstracting tool.')
parser.add_argument('method',
                    type=str,
                    choices=['se', 'ml'],
                    help='Method name')
parser.add_argument('mode',
                    type=str,
                    choices=['f', 'file', 'd', 'dir'],
                    help='Processing mode (f - File, d - Directory)')
parser.add_argument('source',
                    type=str,
                    help='Text source (File(txt), Directory)')
parser.add_argument('-o',
                    '--out',
                    type=str,
                    help='Output path (File, Directory)')
args = parser.parse_args()

if args.method == 'se':
    from methods.se import abstract
else:  # ml
    from methods.ml import abstract

if args.mode in ['f', 'file']:
    file = open(args.source, 'r', encoding='utf-8')
    text = file.read()

    result = abstract(text)

    if result:
        if args.out:
            save_f = open(args.out, 'w', encoding='utf-8')
            save_f.write(str(result))
        else:
            print(f'Result:\n{result}')
else:  # dir
    if args.out and not os.path.exists(args.out):
        os.makedirs(args.out)

    for filename in os.listdir(args.source):
        file = open(f'{args.source}/{filename}', 'r', encoding='utf-8')
        text = file.read()

        result = abstract(text)

        if result:
            if args.out:
                save_f = open(f'{args.out}/{filename}', 'w', encoding='utf-8')
                save_f.write("\n".join(result))
            else:
                print(f'File {filename}. Result:\n{result}\n##########')
