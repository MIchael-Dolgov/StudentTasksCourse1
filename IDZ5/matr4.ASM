;Работает!
;Количество четных элементов ниже главной диагонали.
INCLUDE IO.ASM

MODEL COMPACT

STACK_SEG SEGMENT STACK 'STACK'
    DB 256 DUP (?)
STACK_SEG ENDS

DATA SEGMENT
	cnt dw ?
	matr dw 100 dup(?)
	height dw ?
	widt dw ?
DATA ENDS


CODE SEGMENT
ASSUME SS:STACK_SEG,DS:DATA,CS:CODE   

Start:
	push	ds ;добавляем в стек, т.к данные регистры проца могли использоваться другой программой, поэтому мы кидаем значения в стек
	push	ax
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

	; Ввод значений
	mov cx, ax
	Inizialization:
		inint matr[bx]
		add bx, 2 ;сдвиг по байтам
		loop Inizialization

	;Количество четных элементов ниже главной диагонали.
	mov ax, 1
	mov bx, 0
	mov cnt, 0
	mov cx, height
	repp:
		add bx, widt
		add bx, widt
		loop repp
	sub bx, 4

	mov cx, height
	sub cx, 1
	jcxz escape
	line:
		push cx
		mov cx, widt
		sub cx, ax
		jcxz escape
		items:
			push ax
			mov ax, matr[bx]
			test ax, 1    ; Побитовое AND между AX и 1
			jnz skip
			outint ax
			inc cnt
		skip:
			pop ax
			outint bx, 10
			sub bx, 2
			newline
			loop items
		add ax, 1
		sub bx, ax
		sub bx, ax
		pop cx
		loop line
	escape:

	;Выводит матрицу на экран и
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
	; Вывод числа
	outint cnt,4
;=========================================================
	pop	ax
	pop	ds
Exit:
	finish
ENDS

END	Start