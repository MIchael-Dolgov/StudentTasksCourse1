
INCLUDE IO.ASM

MODEL COMPACT

STACK_SEG SEGMENT STACK 'STACK'
    DB 256 DUP (?)
STACK_SEG ENDS

DATA SEGMENT
	min dw ?
	matr dw 100 dup(?)
	height dw ?
	widt dw ?
DATA ENDS


CODE SEGMENT
ASSUME SS:STACK_SEG,DS:DATA,CS:CODE   

Start:
	push	ds ;
	mov	ax, data
	mov	ds, ax
;==========================CODE=============================
	mov bx, 0
	inint height
	inint widt
	mov ax, 0

	mov cx, widt
	repet:
		add ax, height
		loop repet

	; 
	mov cx, ax
	Inizialization:
		inint matr[bx]
		add bx, 2 ;
		loop Inizialization

	;
	mov ax, 0
	mov bx, 0
	mov dx, widt
	mov min, 32767

	mov cx, height
	line:
		push cx
		mov cx, 0
		add cx, ax
		jcxz new
		items:
			push ax
			mov ax, matr[bx]
			cmp ax, min
			jg skip
			mov min, ax
		skip:
			pop ax
			outint bx, 10
			newline
			add bx, 2
			loop items
		new:
		add bx, dx
		add bx, dx
		sub bx, ax
		sub bx, ax
		add ax, 1
		pop cx
		loop line

	;
	mov bx, 0
	mov cx, height
	ShowWidth:
		push cx
		mov cx, widt
		cycle:
			outint matr[bx], 4
			add bx, 2
			loop cycle

	pop cx
	newline
	loop ShowWidth

	newline
	;
	outint min,4
;=========================================================
	pop	ax
	pop	ds
Exit:
	finish
ENDS

END	Start