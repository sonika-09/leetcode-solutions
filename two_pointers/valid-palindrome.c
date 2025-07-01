//125 - Valid Palindrome
//Runtime = 0ms, Beats = 100%

bool isPalindrome(char* s) {
    int len = strlen(s);
    int j = len - 1;
    int i = 0;
    while (i < j) {
	//we check if the character is an alphanumeric
        if(!isalnum(s[i])) {
            i++;
            continue;
        }
        if(!isalnum(s[j])) {
            j--;
            continue;
        }
	//we make the character lower cased to avoid unnecessary mismatches
        if(tolower(s[i]) != tolower(s[j]))
            return false;
        i++;
        j--;
    }
    return true;
}