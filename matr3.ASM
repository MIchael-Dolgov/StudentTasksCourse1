;Работает!
;Сумму элементов главной и побочной диагонали.
INCLUDE IO.ASM

MODEL COMPACT

ST1 SEGMENT  
	DB 128 DUP(?)
ST1 ENDS

DATA SEGMENT
	matr dw 100 dup(?)
	height dw ?
	widt dw ?
DATA ENDS


CODE SEGMENT
ASSUME SS:ST1,DS:DATA,CS:CODE   

Start:
	push	ds ;добавляем в стек, т.к данные регистры проца могли использоваться другой программой, поэтому мы кидаем значения в стек
	push	ax
	mov	ax, data
	mov	ds, ax
;==========================CODE=============================
;===============НЕ ТРОЖЬ!=============================
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

	; Выводит матрицу на экран
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
;=============================================
	; Главная диагональ
	mov ax, 0
	mov bx, 0
	mov cx, height
	repet1:
		add ax, matr[bx]
		push ax
		mov ax, 0
		add ax, widt
		add ax, widt
		add ax, 2
		add bx, ax
		pop ax
		;add bx, 8 ;3x3 matr
		loop repet1
	outint ax, 4

	newline
	; Побочная диагональ
	mov ax, 0
	mov bx, widt
	add bx, widt
	sub bx, 2
	mov cx, height
	repet2:
		add ax, matr[bx]
		add bx, widt
		add bx, widt
		sub bx, 2
		;add bx, 8 ;3x3 matr
		loop repet2
	outint ax, 4

;=========================================================
	pop	ax
	pop	ds
Exit:
	finish
ENDS

END	Start