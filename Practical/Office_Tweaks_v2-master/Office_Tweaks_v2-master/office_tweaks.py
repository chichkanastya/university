import sys
import cli_parser
import interactive_menu

def main():
    parser = cli_parser.create_parser()
    args = parser.parse_args()
    is_cli_mode = args.pdf2docx or args.docx2pdf or args.compress_images or args.delete

    if args.interactive or not is_cli_mode:
        interactive_menu.start_interactive_mode()
    else:
        cli_parser.handle_cli_args(args)

if __name__ == "__main__":
    main()
