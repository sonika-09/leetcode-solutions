//20 - Valid Parenthesis
//Runtime = 0ms, Beats = 100%

//we define a structure for our stack
typedef struct {
    char *arr;
    int sp;
    int capacity;
}Stack;
//initialize the stack size and the stack's pointer value
void init(Stack *st, int size) {
    st->arr = (char*)malloc(sizeof(char) * size);
    st->sp = -1;
    st->capacity = size;
}
//function to check if stack is empty
bool isEmpty(Stack *st) {
    if (st->sp == -1)
        return true;
    else
        return false;
}
//function to push (only if stack is not full)
void push(Stack *st, char ele) {
    if(st->sp < st->capacity-1) {
        st->sp++;
        st->arr[st->sp] = ele;
    }
    else {
        printf("overflow!");
    }
}
//function to pop out the top element (only if stack is not empty)
//this function's return type could have been void also since we don't use the value of the top element
char pop(Stack *st) {
    char ele = '\0';
    if(!isEmpty(st)) {
        ele = st->arr[st->sp];
        st->sp--;
    }
    return ele;
}
//here is where we check if it's a valid parenthesis or not
bool process(char* s) {
    Stack st;
    int len = strlen(s);
    init(&st, len);
    int i=0;
    while(s[i] != '\0') {
	//whenever there's an opening parenthesis, we push into stack
        if((s[i]=='(') || (s[i]=='[') || (s[i]=='{')) {
            push(&st, s[i]);
        }
	//we pop the top stack element if there's a closing parenthesis
	//but this is only done when the closing and stack top character are of the same kind!
        else if(s[i]==')') {
            if(!isEmpty(&st) && st.arr[st.sp] == '(')
                pop(&st);
            else {
                free(st.arr);
                return false;
            }
        }
        else if(s[i]=='}') {
            if(!isEmpty(&st) && st.arr[st.sp] == '{')
                pop(&st);
            else {
                free(st.arr);
                return false;
            }
        }
        else if(s[i]==']') {
            if(!isEmpty(&st) && st.arr[st.sp] == '[')
                pop(&st);
            else {
                free(st.arr);
                return false;
            }
        }
        else {
            printf("Invalid character!");
            free(st.arr);
            return false;
        }
        i++;
    }
    if(isEmpty(&st)) {
        free(st.arr);
        return true;
    }
    else {
        free(st.arr);
        return false;
    }
}

bool isValid(char* s) {
    return process(s);
}
