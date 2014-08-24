// assumption that all letters are distinct
#include<stdio.h>
#include<malloc.h>
#include<string.h>
char post[100],stack[100];  
int pst,sptr, rst,inord=0, clcnt,resflag; // points to the current values in post and stack
char cnfform[100];
char clause[100][100];
typedef struct node {
	char a;
	int flag;
	struct node *left;
	struct node *right;
} node;

void rem_extra(int i){
	int len = strlen(clause[i])+1,j,k,a;
	for(k=0;k<len;k++){
		for(j=k+1;j<len;j++){
			if(clause[i][k] == clause[i][j]){
				len--;
				for(a=k;a<len;a++)
					clause[i][a] = clause[i][a+1];
			}
		}
	}
	for(k=0;k<len;k++){
		for(j=k+1;j<len;j++){
			if(abs(clause[i][k]- clause[i][j]) == 32){
				len--;
				for(a=j;a<len;a++)
					clause[i][a] = clause[i][a+1];
				len--;
				for(a=k;a<len;a++)
					clause[i][a] = clause[i][a+1];
			}
		}
	}
}

void sorting(int j){
	int l,m,n,k,i;
	char tem;
	for(i=0;i<j+1;i++){                      // j stores the total number of clauses
		for(k=0;k<strlen(clause[i]);k++){
			for(l=0;l<strlen(clause[i])-1;l++){
				if(clause[i][l]>clause[i][l+1]){
					tem = clause[i][l];
					clause[i][l] = clause[i][l+1];
					clause[i][l+1] = tem;
				}
			}
		}
	}
}

node *copytree(node *head){
	if(head!=NULL){
	node *copy;
	copy = (node *)malloc(sizeof (node ));

	copy->a = head->a;
	copy->flag = head->flag;

	node *left,*right;
	if(head->left)
		copy->left = copytree(head->left);
	if(head->right)
		copy->right = copytree(head->right);

	return copy;
	}
}


void lining(){
	int a=0,i,k;
	for(i=0;i<clcnt;i++){
		if( strlen(clause[i]) == 0){
			clcnt--;
			for(a=i;a<clcnt;a++)
				strcpy(clause[a],clause[a+1]);
			//		continue;
			i--;
		}
		for(k=i+1;k<clcnt;k++){
			if(strcmp(clause[i],clause[k])==0){
				clcnt--;
				for(a=k;a<clcnt;a++)
					strcpy(clause[a],clause[a+1]);
			}
		}
	}
}

int resol(int i,int j){
	int leni = strlen(clause[i])+1;
	int lenj = strlen(clause[j])+1;
	char stri[100],strj[100];
	strcpy(stri,clause[i]);
	strcpy(strj,clause[j]);
	int a,b,c;
	int unity=0;
	for(a=0;a<leni;a++){
		for(b=0;b<lenj;b++){
			if(abs(stri[a]-strj[b]) == 32){
				leni--;
				for(c=a;c<leni;c++)
					stri[c] = stri[c+1];
				lenj--;
				for(c=b;c<lenj;c++)
					strj[c] = strj[c+1];
				a--;
				b--;
				unity++;
			}
		}
	}
	
	if(strlen(stri)==0 && strlen(strj)==0 && unity==1){
			resflag = 1;
			return;
	}
	if(unity == 1){
	char *res = strcat(stri,strj);
		//printf("before resolving %s\n",res);
	if(strlen(res) >= (strlen(clause[i]) + strlen(clause[j]))){
		return -1;
	}else{
		//printf("inside resolving %s\n",res);
		int k,l;
		char tem;
		strcpy(clause[clcnt],res);
		for(k=0;k<strlen(clause[clcnt]);k++){
			for(l=0;l<strlen(clause[clcnt])-1;l++){
				if(clause[clcnt][l]>clause[clcnt][l+1]){
					tem = clause[clcnt][l];
					clause[clcnt][l] = clause[clcnt][l+1];
					clause[clcnt][l+1] = tem;
				}
			}
		}
		rem_extra(clcnt);
		if(strlen(clause[clcnt]) == 0){
			clcnt--;
			return 1;
		}else{
		clcnt++;
		}
		//printf("inside resolving %s\n",res);
		lining();
		return 1;
	}
	}
}

void inordertoarray(node *head){
	if(head!=NULL){
		inordertoarray(head->left);
		if( head->flag == -1 ){
			if( head->a == '|'){
				cnfform[inord++] = '^';
			}else if( head->a == '^'){
				cnfform[inord++] = '|';
			}else if( head->a == '|'){
				cnfform[inord++] = '^';
			}else{
				cnfform[inord++] = '~';
				cnfform[inord++] = head->a;
			}
		}else{
			cnfform[inord++] = head->a;
		}
		inordertoarray(head->right);
	}
}
void inorder(node *head){
	if(head!=NULL){
		inorder(head->left);
		//printf("%c f=%d ", head->a,head->flag);
		inorder(head->right);
	}
}
node *cnf(node *head){
	if(head->left)
		head->left = cnf(head->left);
	if(head->right)
		head->right = cnf(head->right);
	if((head->a == '|' && head->flag == 1) || (head->a == '^' && head->flag == -1)){
		if((head->left->a == '|' && head->left->flag == -1) || (head->left->a == '^' && head->left->flag == 1)){
			if((head->right->a == '|' && head->right->flag == -1) || (head->right->a == '^' && head->right->flag == 1)){
				node *a,*b,*c,*d;
				a = head->left->left;
				b = head->left->right;
				c = head->right->left;
				d = head->right->right;
				node *a2,*b2,*c2,*d2;
				a2 = copytree(a);	
				b2 = copytree(b);	
				c2 = copytree(c);	
				d2 = copytree(d);	
				head->a = '^';
				head->flag = 1;
				node *new_left,*new_right;
				node *new_left_left,*new_left_right,*new_right_left,*new_right_right;
				new_left = (node *)malloc(sizeof (node ));
				new_right = (node *)malloc(sizeof (node));
				new_left_left = (node *)malloc(sizeof (node ));
				new_left_right = (node *)malloc(sizeof (node ));
				new_right_left = (node *)malloc(sizeof (node));
				new_right_right = (node *)malloc(sizeof (node));
				new_left_left->a = '|';
				new_left_left->flag = 1;
				new_left_right->a = '|';
				new_left_right->flag = 1;
				new_right_left->a = '|';
				new_right_left->flag = 1;
				new_right_right->a = '|';
				new_right_right->flag = 1;
				new_left->a = '^';
				new_left->flag = 1;
				new_right->a = '^';
				new_right->flag = 1;
				new_left->left = new_left_left;
				new_left->right = new_left_right;
				new_right->left = new_right_left;
				new_right->right = new_right_right;
				new_left_left->left = a;
				new_left_left->right = c;
				new_left_right->left = b;
				new_left_right->right = c2;
				new_right_left->left = a2;
				new_right_left->right = d;
				new_right_right->left = b2;
				new_right_right->right = d2;
				head->left = new_left;
				head->right = new_right;
				return head;
			}else{
				head->a = '^';
				head->flag = 1;
				node *a,*b,*c;
				a = head->left->left;
				b = head->left->right;
				c = head->right;
				node *c2;
				c2 = copytree(c);
				node *new_left,*new_right;
				new_left = (node *)malloc(sizeof (node ));
				new_right = (node *)malloc(sizeof (node));
				new_left->a = '|';
				new_left->flag = 1;
				new_right->a = '|';
				new_right->flag = 1;
				new_left->left = a;
				new_left->right = c;
				new_right->left = b;
				new_right->right = c2;
				head->left = new_left;
				head->right = new_right;
				return head;
			}
		}
		if((head->right->a == '|' && head->right->flag == -1) || (head->right->a == '^' && head->right->flag == 1)){
			head->a = '^';
			head->flag = 1;
			node *a,*b,*c;
			a = head->right->left;
			b = head->right->right;
			c = head->left;
			node *c2;
			c2 = copytree(c);
			node *new_left,*new_right;
			new_left = (node *)malloc(sizeof (node ));
			new_right = (node *)malloc(sizeof (node));
			new_left->a = '|';
			new_left->flag = 1;
			new_right->a = '|';
			new_right->flag = 1;
			new_left->left = a;
			new_left->right = c;
			new_right->left = b;
			new_right->right = c2;
			head->left = new_left;
			head->right = new_right;
			return head;
		}
	}
	return head;
}

void propagate_neg(node *head){
	if(head->left)
		propagate_neg(head->left);
	head->flag *= -1;
	if(head->right )
		propagate_neg(head->right);
}

node *remove_neg(node *head){
	if(head->left){
		head->left = remove_neg(head->left);
	}
	if(head->right){
		head->right = remove_neg(head->right);
	}
	if(head->a == '~'){
		propagate_neg(head->right);
	}
	if(head->a == '~')
		return head->right;
	return head;
}

void insert(inp){

	if(sptr == -1){
		sptr++;
		stack[sptr] = inp;
		return;
	}
	if(inp == '('){
		sptr++;
		stack[sptr] = inp;
	}else if(inp == ')'){
		while(stack[sptr]!='('){
			pst++;
			post[pst] = stack[sptr];
			sptr--;
		}
		sptr--; // erasing the (
	}else if(inp == '~'){
		if(stack[sptr] == '('){
			sptr++;
			stack[sptr] = inp;
		}else if(stack[sptr] == '~'){
			pst++;
			post[pst] = stack[sptr];
		}else{
			sptr++;
			stack[sptr] = inp;
		}
	}else if(inp == '^'){
		if(stack[sptr] == '('){
			sptr++;
			stack[sptr] = inp;
		}else if(stack[sptr] == '^'){
			pst++;
			post[pst] = stack[sptr];
		}else if(stack[sptr] == '~'){
			pst++;
			post[pst] = stack[sptr];
			sptr--;
			insert(inp);
		}else {
			sptr++;
			stack[sptr] = inp;
		}
	}else if(inp == '|'){
		if(stack[sptr] == '('){
			sptr++;
			stack[sptr] = inp;
		}else if(stack[sptr] == '|'){
			pst++;
			post[pst] = stack[sptr];
		}else if(stack[sptr] == '~' || stack[sptr] == '^'){
			pst++;
			post[pst] = stack[sptr];
			sptr--;
			insert(inp);
		}else{
			sptr++;
			stack[sptr] = inp;
		}
	}else if(inp == '-'){
		if(stack[sptr] == '('){
			sptr++;
			stack[sptr] = inp;
		}else if(stack[sptr] == '-'){
			pst++;
			post[pst] = stack[sptr];
		}else if(stack[sptr] == '~' || stack[sptr] == '^' || stack[sptr]=='|'){
			pst++;
			post[pst] = stack[sptr];
			sptr--;
			insert(inp);
		}else{
			sptr++;
			stack[sptr] = inp;
		}
	}else if(inp == '<'){
		if(stack[sptr] == '('){
			sptr++;
			stack[sptr] = inp;
		}else if(stack[sptr] == '<'){
			pst++;
			post[pst] = stack[sptr];
		}else if(stack[sptr] == '~' || stack[sptr] == '^' || stack[sptr]=='|' || stack[sptr]=='-' ){
			pst++;
			post[pst] = stack[sptr];
			sptr--;
			insert(inp);
		}else{
			sptr++;
			stack[sptr] = inp;
		}
	}
}




int main(){
	int shuru,hogaya;
	scanf("%d",&shuru);
	for(hogaya = 0;hogaya<shuru;hogaya++){
		int i,t;
		clcnt = 0;
		pst = -1;
		sptr = -1;
		rst = 0;
		inord = 0;
		char inp[100],temp[100];
		scanf("%s", inp);
		for(i=0;i<strlen(inp);i++){                                       
			if(inp[i]=='<' && inp[i+1] =='-' && inp[i+2]=='>')        
				inp[i+1]='>';                                     
		}                       

		// changing the input
		temp[0]='(';
		t = 1;  // points to the next free value in temp
		for(i=0;i<strlen(inp);i++){
			if(inp[i] == '='){
				if(i==0){
					temp[t] = '(';
					t++;
				temp[t] = '~';
				t++;
					temp[t] = '(';
					t++;	
					i++;
					continue;
				}
				temp[t] = ')';
				t++;
				temp[t] = '^';
				t++;
				temp[t] = '(';
				t++;
				temp[t] = '~';
				t++;
				temp[t] = '(';
				t++;
				temp[t] = '(';
				t++;
				i++;
			}else if(inp[i] == ','){
				temp[t] = ')';
				t++;
				temp[t] = '^';
				t++;
				temp[t] = '(';
				t++;
			}else{
				temp[t] = inp[i];
				t++;
			}
		}
		temp[t]=')';
		temp[t+1]=')';
		temp[t+2]=')';
		temp[t+3]='\0';
		strcpy(inp,temp);
		for(i=0;i<strlen(inp);i++){
			if(inp[i]=='(' || inp[i]==')' || inp[i]=='~' || inp[i]=='^' || inp[i]=='|' || inp[i]=='-' || inp[i]=='>' || inp[i]=='=' || inp[i]=='<' ){
				if(inp[i] == '='){
					i += 2;
					break;
				}
				insert(inp[i]);	
			}else{
				pst++;
				post[pst]=inp[i];
			}
		}
		int j = i;
		for(i=sptr;i>=0;i--){
			pst++;
			post[pst] = stack[i];
		}
		char lhs[100];
		int llen=pst+1;
		for(i=0;i<pst+1;i++){
			lhs[i] = post[i];
		}
		node *head[100];
		head[0] = (node *)malloc(sizeof (node));
		head[0]->left = NULL;
		head[0]->right = NULL;
		t = 0; // pointer to the current occupied queue of the tree nodes
		node *new;
		new = (node *)malloc(sizeof (node));
		new->a = lhs[0];
		new->flag = 1;
		new->right = NULL;
		new->left = NULL;
		head[0]->left = new;
		for(i=1;i<llen;i++){
			if(lhs[i]=='~'){
				node *new;
				new = (node *)malloc(sizeof (node));
				new->a = '~';
				new->flag = 1;
				new->right = head[t]->left;
				new->left =NULL;
				head[t]->left = new;
			}else if(lhs[i]=='^'){
				node *new;
				new = (node *)malloc(sizeof (node));
				new->a = '^';
				new->flag = 1;
				new->right = head[t]->left;
				t--;
				new->left = head[t]->left;
				head[t]->left = new;
			}else if(lhs[i]=='|'){
				node *new;
				new = (node *)malloc(sizeof (node));
				new->a = '|';
				new->flag = 1;
				new->right = head[t]->left;
				t--;
				new->left =head[t]->left;
				head[t]->left = new;
			}else if(lhs[i]=='-'){
				node *new;
				new = (node *)malloc(sizeof (node));
				node *neg;
				neg = (node *)malloc(sizeof (node));
				neg->a = '~';
				neg->flag = 1;
				new->a = '|';
				new->flag = 1;
				new->right = head[t]->left;
				t--;
				new->left = neg;
				neg->right = head[t]->left;
				head[t]->left = new;
			}else if(lhs[i]=='<'){
				node *a,*b,*a2,*b2;
				a = head[t]->left;
				a2 = copytree(a);
				node *new;
				new = (node *)malloc(sizeof (node));
				node *new_left;
				new_left = (node *)malloc(sizeof (node));
				node *new_right;
				new_right = (node *)malloc(sizeof (node));
				node *neg_right;
				neg_right = (node *)malloc(sizeof (node));
				node *neg_left;
				neg_left = (node *)malloc(sizeof (node));
				neg_right->left = NULL;  // q
				neg_left->left = NULL;  // q
				neg_left->a = '~';
				neg_right->a = '~';
				neg_right->flag = 1;
				neg_left->flag = 1;
				new->a = '^';
				new->flag = 1;
				new_left->a = '|';
				new_left->flag = 1;
				new_right->a = '|';
				new_right->flag = 1;
				new_left->left = neg_left;
				new_right->left = neg_right;
				neg_left->right = a;  // q
				new_right->right = a2;
				new->left = new_left;
				new->right = new_right;
				t--;
				b = head[t]->left;
				b2 = copytree(b);
				neg_right->right = b;
				new_left->right = b2;
			//	printf("LLOOOKKK HERE %c",head[t]->left->a);
				head[t]->left = new;
			}else{
				t++;
				head[t] = (node *)malloc(sizeof (node));
				head[t]->left =NULL;
				head[t]->right =NULL;
				node *new;
				new = (node *)malloc(sizeof (node));
				new->a = lhs[i];
				new->flag = 1;
				new->right = NULL;
				new->left = NULL;
				head[t]->left = new;
			}		
		}
		//printf("t = %d\n",t);
		inorder(head[t]);
		//printf("\n");
		head[t]->left = remove_neg(head[t]->left);  // negations are removed also
		head[t] = cnf(head[t]);
		inorder(head[t]);
		inordertoarray(head[t]);
		//printf("\n");
		//for(i=0;i<inord;i++)
		//		printf("%c  ",cnfform[i]);
		//	printf("\n");
			j=0;					// points to the next free position in the clause array
		int k =0;  				// points to the position of the second variable
		for(i=0;i<inord;i++){  			// taking out the clauses
			if(cnfform[i] == '|')
				continue;
			if(cnfform[i] == '~'){
				i++;
				if(cnfform[i]>90){
					clause[j][k++] = cnfform[i]-32;
				}else{
					clause[j][k++] = cnfform[i]+32;
				}
				continue;
			}
			if(cnfform[i] == '^'){
		//		printf("clause first %s\n",clause[j]);
				clause[j][k]='\0';
				j++;
				k=0;
				continue;
			}
			clause[j][k++] = cnfform[i];
		}
		//printf("\n");
		//printf("\n");
	//	printf("\n");
	//	printf("\n");
		int l,m,n;
		char tem;
		clcnt = j+1;
		sorting(clcnt);
		for(i=0;i<clcnt;i++){
			rem_extra(i);
	//		printf("%s\n",clause[i]);
		}
		int a=0;
		lining();
	//	printf("\n");
	//	for(i=0;i<clcnt;i++)
	//	printf("%s\n",clause[i]);
		int q,w;
		resflag=0;
		for(k=0;k<clcnt;k++){	
			for(i=0;i<clcnt;i++){
				for(j=0;j<clcnt;j++){
					w=clcnt;
					q=resol(i,j);
					if(resflag==1)
						break;
				}
				if(resflag==1)
					break;
			}
			if(resflag==1)
				break;
		}
	//	printf("\n");
	//	for(i=0;i<clcnt;i++)
	//	printf("%s\n",clause[i]);
		if(resflag==0){
			printf("0\n");
		}else{
			printf("1\n");
		}
		printf("\n");
	}
}
// assuming that rhs does not contain a tautology :P, ie sumtin like p|~p
