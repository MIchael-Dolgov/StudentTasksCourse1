;Работает!
;Максимальный элемент выше главной диагонали.
INCLUDE IO.ASM

MODEL COMPACT

STACK_SEG SEGMENT STACK 'STACK'
    DB 256 DUP (?)
STACK_SEG ENDS

DATA SEGMENT
	max dw ?
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

	; Поиск максимального
	mov ax, 1
	mov bx, 0
	mov max, -32768

	mov cx, height
	line:
		push cx
		mov cx, widt
		jcxz escape
		sub cx, ax
		jcxz escape
		items:
			push ax
			mov ax, matr[bx]
			cmp ax, max
			jl skip
			mov max, ax
		skip:
			pop ax
			outint bx, 10
			newline
			add bx, 2
			loop items
		add bx, ax
		add bx, ax
		add ax, 1
		pop cx
		loopnz line
	escape:

	;Выводит матрицу на экран и
	;Максимальный элемент выше главной диагонали.
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
	outint max,4
;=========================================================
	pop	ax
	pop	ds
Exit:
	finish
ENDS

END	Start