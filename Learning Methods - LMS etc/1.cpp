class Dataset{

	  // Assume that the data file is plain text with each row
	  // containing the class label followed by the features, 
	  // separated by blank spaces.
	  bool readData(filename);

	    // Write data in the above format.
	    bool writeData(filename);

	      // Variables for data
	      vector<DataItem*> data;
	        ...
};

bool Dataset::readData(char *filename){
}
