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
    with open(args.source, 'r', encoding='utf-8') as file:
        text = file.read()
        result = abstract(text)
        if result:
            if args.out:
                with open(args.out, 'w', encoding='utf-8') as save_f:
                    save_f.write("\n".join([str(x) for x in result]))
            else:
                print(f'Result:\n{result}')
        else:
            print('No result.')
elif args.mode in ['d', 'dir']:
    if args.out and not os.path.exists(args.out):
        os.makedirs(args.out)
    for filename in os.listdir(args.source):
        with open(f'{args.source}/{filename}', 'r', encoding='utf-8') as file:
            text = file.read()
            result = abstract(text)
            if result:
                if args.out:
                    with open(f'{args.out}/{filename}', 'w', encoding='utf-8') as save_f:
                        save_f.write("\n".join([str(x) for x in result]))
                else:
                    print(f'File {filename}. Result:\n{result}\n##########')
            else:
                print(f'File {filename}. Result: No result.\n##########')
