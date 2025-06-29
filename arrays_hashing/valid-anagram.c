//242 - valid anagram
//Runtime = 0ms, Beats = 100%

bool isAnagram(char* s, char* t) {
	//checks if strings are of equal length
    if (strlen(s) != strlen(t))
        return false;

    int n = strlen(s);
    int countS[26], countT[26];

	//make HashMap for both strings
	// ASCII value of a is 97
    for(int i=0; i<n; i++) {
        countS[s[i] - 97] = countS[s[i] - 97] + 1;
        countT[t[i] - 97] = countT[t[i] - 97] + 1;
    }   

	//check if HashMap for both strings is equal 
    for(int j=0; j<26; j++) {
        if(countS[j] != countT[j])
            return false;
    }
    return true;
}


//here's another method that I tried initially, it's not as efficient
//Runtime = 27ms, Beats = 12.82%
int compare (const void* a, const void* b) {
    return (*(const char*)a - *(const char*)b);
}

bool isAnagram(char* s, char* t) {
    int flag;
	//we sort the strings are compare them
    qsort(s, strlen(s), sizeof(s[0]), compare);
    qsort(t, strlen(t), sizeof(t[0]), compare);
    flag = strcmp(s, t);
    if (flag != 0)
        return false;
    return true;
}
