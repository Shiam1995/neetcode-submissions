class Solution {
public:
    bool isAnagram(string s, string t) {
        //bubble sort is dumb
        // check letter for letter is dumb
        // delete - block 
        // changing word 
        // 3 solution 1 opitmal

        string s_copy = s;
        string t_copy = t;

        //std::cout << s_copy << std::endl;
        //std::cout << t_copy << std::endl;

        for (int i = 0; i < s.size(); i++){
            for (int j = 0; j < s.size(); j++){

                if(s_copy[i] == t_copy[j])
                {
                    s_copy[i] = 0;
                    t_copy[j] = 0;
                    break;
                }
            }
        }
        
        if (s_copy == t_copy)
        {
            return true;
        }else{
            return false;
        }

        



    }

    
};
