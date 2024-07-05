#include <bits/stdc++.h>
using namespace std;

//a, b, c đại diện cho 3 thanh ghi
deque<char> a;
deque<char> b;
deque<char> c;

//stream_key: key được sinh ra
string IV, key;

string bin_to_text(const vector<char> &bits) {
    string ascii;
    for (int i = 0; i < bits.size(); i += 8) {
        char byte = 0;
        for (int j = 0; j < 8; j++) {
            byte |= (bits[i + j] << (7 - j));
        }
        ascii += byte;
    }
    return ascii;
}

vector<char> xor_two_binary(const vector<char>& bits1,
                            const vector<char>& bits2) {
    vector<char> result;
    size_t size = bits1.size();

    for (size_t i = 0; i < size; ++i) {
        result.push_back(bits1[i] ^ bits2[i]);
    }
    return result;
}

vector<char> string_to_binary(const string &content) {
    vector<char> bits;
    for (char c : content) {
        // Chuyển ký tự thành mã ASCII
        int asciiValue = static_cast<int>(c);

        // Chuyển mã ASCII thành dãy bit và đưa vào vector
        bitset<8> bitset(asciiValue);
        for (int i = 7; i >= 0; --i) {
            bits.push_back(bitset[i]);
        }
    }
    return bits;
}

void warm_up() {
    for (int i = 0; i < 1152; i++){
        a.push_front(c[65] ^ c[110] ^ (c[108]&&c[109]) ^ a[68]);
        if (a.size() > 93) a.pop_back();
        if (a.size() == 93) {
            b.push_front(a[65] ^ a[92] ^ (a[90] && a[91]) ^ b[77]);
            if (b.size() > 84) b.pop_back();
        }
        if (b.size() == 84) {
            c.push_front(b[68] ^ b[83] ^ (b[81] && b[82]) ^ c[86]);
            c.pop_back();
        }
    }
}

vector<char> encryption(int size) {
    vector<char> stream_key;
    for (int i = 0; i < size; i++){
        char x = a[65] ^ a[92] ^ (a[90] && a[91]);
        char y = b[68] ^ b[83] ^ (b[81] && b[82]);
        char z = c[65] ^ c[110] ^ (c[108]&&c[109]);

        stream_key.push_back(x ^ y ^ z);

        a.push_front(z ^ a[68]);
        a.pop_back();

        b.push_front(x ^ b[77]);
        b.pop_back();

        c.push_front(y ^ c[86]);
        c.pop_back();
    }
    return stream_key;
}

void cipher(char* read, char* write) {
    FILE *fread = fopen(read, "r");
    FILE *fwrite = fopen(write, "w");
    string content;
    char buffer[256];
    while (fgets(buffer, sizeof(buffer), fread) != nullptr) {
        content += buffer;
    }

    vector<char> stream_key = encryption(content.size()*8);
    vector<char> bin_content = string_to_binary(content);
    vector<char> encrypted = xor_two_binary(bin_content, stream_key);
    string result = bin_to_text(encrypted);
    fputs(result.c_str(), fwrite);
    fclose(fread);
    fclose(fwrite);
}

int main() {
    IV = "1010101011001100111100001111000011110000111100001111000011110000111100001111000011110000111100001111";
    key = "110011000111100000111100001111000011110000111100001111000011110000111100001111000011110000111100001111";

    for(int i = 0; i < 80; i++) {
            a.push_back(IV[i] - '0');
            b.push_back(key[i]- '0');
    }

    c.assign(111, 0);
    c[108] = 1;
    c[109] = 1;
    c[110] = 1;
    warm_up();

    FILE *read = fopen("read.txt", "r");
    FILE *write = fopen("write.txt", "w");

    string content;
    char buffer[256];
    while (fgets(buffer, sizeof(buffer), read) != nullptr) {
        content += buffer;
    }
    fputs(content.c_str(), write);

    fclose(read);
    fclose(write);

    vector<char> bit_content = {0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0};

//    for (char c : content) {
//        // Chuyển ký tự thành mã ASCII
//        int asciiValue = static_cast<int>(c);
//
//        // Chuyển mã ASCII thành dãy bit và đưa vào vector
//        bitset<8> bitset(asciiValue);
//        for (int i = 7; i >= 0; --i) {
//            bit_content.push_back(bitset[i]);
//        }
//    }
//
//    for (char c : bit_content) cout << int(c) << " ";

    return 0;
}
