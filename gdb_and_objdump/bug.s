.global main
main:
    jmpl   *(%eax)  # near jump to 32bit address in (%eax) (relative to next instruction in the same segment)
    jmpw   *(%eax)  # near jump to 16bit address in (%eax) (relative to next instruction in the same segment)
    ljmpl  *(%eax)  # far  jump to 48bit address in (%eax) (uses  16 bits for segment and 32 bits for offset)
    ljmpw  *(%eax)  # far  jump to 32bit address in (%eax) (uses  16 bits for segment and 16 bits for offset)

# Let's first assemble this (without linking):  gcc -m32 -c test.s
# Now, let's disassemble the object file test.o using objdump and intel syntax: objdump -d -M intel test.o
# We see that the disassembling confuses the first and last instructions as the same instruction "jmp DWORD PTR [eax]".

# output of objdump:
# 00000000 <test>:
#    0:   ff 20                   jmp    DWORD PTR [eax]
#    2:   66 ff 20                jmp    WORD PTR [eax]
#    5:   ff 28                   jmp    FWORD PTR [eax]
#    7:   66 ff 28                jmp    DWORD PTR [eax]

# The instruction "jmp DWORD PTR [eax]" actual encoding corresponds to the first but not the last instruction above.
# GDB shows similar results when using intel syntax, but other disassemblers such as Capstone don't have this problem.
# Reference 1: online capestone disassembler (http://shell-storm.org/online/Online-Assembler-and-Disassembler)
# Reference 2: jump instruction reference (https://www.felixcloutier.com/x86/jmp)
