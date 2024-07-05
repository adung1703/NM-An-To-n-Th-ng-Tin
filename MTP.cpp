#include <iostream>
#include <string>

using namespace std;

int char_to_int(char c) { //Chuyen ky tu hex sang gia tri tuong ung. Vi du 'a' -> 10
    if (c >= 'a') return c - 'a' + 10;
    else if (c >= 'A') return c - 'A' + 10;
    else return c - '0';
}

char int_to_hex(int n) { //Chuyen so sang char tuong ung
    if (n >= 10) return 'a' + (n - 10);
    else return '0' + n;
}

string xor_hex_strings(string s1, string s2) {
    while (s1.length() > s2.length()) s1.pop_back();
    while (s1.length() < s2.length()) s2.pop_back();
    int length = s1.length();
    string res;
    for (int i = 0; i < length; i++) {
        int c = char_to_int(s1[i]) ^ char_to_int(s2[i]);
        res.push_back(int_to_hex(c));
    }
    
//    for (int i = 0; i < length; i += 2) { //Loai bo nhung ky tu khong nam trong A-Za-z va thay the bang '-' cho de nhin
//        if ((res[i] < '4') 
//		|| (res[i] == '4' && res[i+1] == '0') 
//		|| (res[i] > '7') 
//		|| (res[i] == '7' && res[i+1] > 'A')) {
//        	res[i] = '2';
//        	res[i+1] = 'D';
//		}
//    }
    
    return res;
}

char hex_to_char(string hex) {
    int value = stoi(hex, nullptr, 16);
    return static_cast<char>(value);
}

string hex_to_text(string hex_string) { //chuyen hex to text
    string text;
    for (size_t i = 0; i < hex_string.length(); i += 2) {
        string hex_byte = hex_string.substr(i, 2);
        char character = hex_to_char(hex_byte);
        text.push_back(character);
    }
    return text;
}

int main() {
	string x[11];
    x[0] = "315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba50";
    x[1] = "234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb741";
    x[2] = "32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de812";
    x[3] = "32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee41";
    x[4] = "3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de812";
	x[5] = "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d";
	x[6] = "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af513";
	x[7] = "315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e941";
	x[8] = "271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f404";
	x[9] = "466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d";
    x[10] = "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904";
    
    for (int i = 0; i < 11; i++) {
    	for (int j = 0; j < 11; j++) {
    		if (i == j) continue;
    		cout << "X" << i+1 << " xor X" << j+1;
			if (i < 9) cout << " ";
			if (j < 9) cout << " ";
			cout << ": " << hex_to_text(xor_hex_strings(x[i], x[j]))  << endl;
		}
		cout << endl;
	} // Xor tung cap mot
	
	
	// Tim key
	cout << hex_to_text(xor_hex_strings(x[3],"54686520636970686572746578742070726F64756365642062792061207765616B20656E6372797074696F6E20616C676F726974686D206C6F6F6B7320617320676F6F64206173206369706865727465787420"));
	
	// Ket qua can tim
	cout << hex_to_text(xor_hex_strings(x[10],"66396e89c9dbd8cc9874352acd6395102eafce78aa7fed28a07f6bc98d29c50b69b0339a19f8aa401a9c6d708f80c066c763fef0123148cdd8e802d05ba98777335daefcecd59c433a6b268b60bf4ef03c9a61"));
	
    return 0;
}

