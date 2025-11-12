import time
import sys
def bf(code, input_tape, input_auto_zero, num_zeros=10):
    input_read_pos = 0
    tape = [0] * num_zeros
    tickerpos = 0
    added_zeroes = 0
    last_print = "input"
    def_steps = 0
    debug_steps = 0

    def remove_non_commands(code):
        commands = list("><+-.,[]?!%")
        return ''.join(c for c in code if c in commands)
    
    code = remove_non_commands(code)
    i = 0
    while i < len(code):
        char = code[i]
        
        if char == '>':
            def_steps += 1
            tickerpos += 1
            if tickerpos >= num_zeros:
                num_zeros += 1
                tape.append(0) 
                added_zeroes += 1
        elif char == '<':
            def_steps += 1
            tickerpos -= 1
            if tickerpos < 0:
                tape.insert(0, 0)
                tickerpos += 1
                added_zeroes += 1
        elif char == '+':
            def_steps += 1
            tape[tickerpos] = (tape[tickerpos] + 1) % 256
        elif char == '-':
            def_steps += 1
            tape[tickerpos] = (tape[tickerpos] - 1) % 256
        elif char == '?':
            debug_steps += 1
            if last_print == "output": print("")
            yup = [chr(x) if chr(x) != '\x00' else ' ' for x in tape]
            print(str(yup).replace("'", '').replace(",", ''))
            if 0 <= tickerpos <= len(tape)-1:
                posh = 1
                ok = tickerpos
                for char in range(ok):
                    posh += 2
                print(' ' * posh + '^')
            else:
                print(tickerpos)

            print(str(tape).replace(",", ""))
            if 0 <= tickerpos <= len(tape)-1:
                pos = 1  
                for k, val in enumerate(tape):
                    if k == tickerpos:
                        break
                    pos += len(str(val))
                    if k < len(tape) - 1:
                        pos += 1
                print(' ' * pos + '^')
            else:
                print(tickerpos)
            last_print = "debug"
        elif char == '.':
            def_steps += 1
            print(chr(tape[tickerpos]), end='')
            last_print = "output"
        elif char == ',':
            def_steps += 1
            if len(input_tape) <= input_read_pos and not input_auto_zero:
                if last_print == "output": print("")
                input_tape += input("input: ")

            if len(input_tape) > input_read_pos:
                tape[tickerpos] = ord(input_tape[input_read_pos]) % 256
                input_read_pos += 1
            else:
                tape[tickerpos] = 0
            last_print = "input"
            
        elif char == '[':
            def_steps += 1
            if tape[tickerpos] == 0:
                    # find matching ]
                    count = 1
                    i
                    while count > 0:
                        i += 1
                        if code[i] == "[":
                            count += 1
                        elif code[i] == "]":
                            count -= 1
        elif char == ']':
            def_steps += 1
            if tape[tickerpos] != 0:
                    # find matching [
                    count = 1
                    while count > 0:
                        i -= 1
                        if code[i] == "]":
                            count += 1
                        elif code[i] == "[":
                            count -= 1
        elif char == "!":
            debug_steps += 1
            if last_print == "output": print("")
            print(f"Commands: {len(code)}")
            print(f"Added zeroes: {added_zeroes}")
            print(f"Steps ran: {def_steps}")
            print(f"Debug steps ran: {debug_steps}")
        elif char == "%":
            time.sleep(0.1)
        else:
            pass
        i += 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_tape = sys.argv[2] if (len(sys.argv) > 2 and sys.argv[2][0:2] != "--") else ""
        input_auto_zero = False if input_tape == "" else True

        with open(sys.argv[1], 'r') as file:
            bf(file.read(), input_tape=input_tape, input_auto_zero=input_auto_zero)
    else:
        print("Usage: python bf_intp.py [file] [args]")