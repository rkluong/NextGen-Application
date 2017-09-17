//
//  Sports_ViewController.swift
//  NextGen
//
//  Created by Mahamadou Sylla on 2/21/17.
//  Copyright © 2017 Mahamadou Sylla. All rights reserved.
//

import UIKit
import Foundation



class Sports_ViewController: UIViewController,
 UITableViewDelegate, UITableViewDataSource {
    
    var buttonClicked = String()
    var tableViewDataSource : [Dictionary<String, String>] = [];
    @IBOutlet weak var tableView: UITableView!
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        var s = "http://www.masisnguyen.com/randy/mysql_proxy.php?command=SELECTT%20*%20FROM%20"
        
        let url = URL(string: s + buttonClicked  + "%20ORDER%20BY%20eventDate%20ASC")
        
        let task = URLSession.shared.dataTask(with: url!) { data, response, error in
            guard error == nil else {
                print(error!)
                return
            }
            guard let data = data else {
                print("Data is empty")
                return
            }
            
            let json = try! JSONSerialization.jsonObject(with: data, options: []) as! [String:AnyObject]
            
            let myData = (json["data"] as! NSArray) as Array
            for dict in myData {
                self.tableViewDataSource.append(dict as! [String: String])
            }
            
            print(self.tableViewDataSource)
            self.tableView.reloadData()
        }
        
        
        
        task.resume()
        
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    
    
        // return the size of the array to tableview
        func tableView(_ tableView: UITableView,numberOfRowsInSection section: Int) -> Int {
            return tableViewDataSource.count
        }
    
        // assign the values in your array variable to cells
        func tableView(_ tableView: UITableView,
                       cellForRowAt indexPath: IndexPath) ->
            UITableViewCell {
    
                // get a reference to our storyboard cell
                let cell = self.tableView.dequeueReusableCell(withIdentifier: "customCell", for: indexPath) as! Sports_TableViewCell

                
            
                var dict = tableViewDataSource[indexPath.row]
                var a : String!
                a = dict["eventDate"]
                var b : String!
                b = dict["location"]
                var c : String!
                c = dict["opponent"]
                var d : String!
                d = dict["score"]
                var e : String!
                e = dict["eventTime"]

                cell.dataLabel!.text = a + " " + b + " " + c + " " + d + " " + e
                
    
                return cell;
        }
    

    


    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
