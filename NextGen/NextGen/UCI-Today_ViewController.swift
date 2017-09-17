//
//  UCI-Today_ViewController.swift
//  NextGen
//
//  Created by Mahamadou Sylla on 2/21/17.
//  Copyright © 2017 Mahamadou Sylla. All rights reserved.
//

import UIKit

class UCI_Today_ViewController: UIViewController,
 UITableViewDelegate, UITableViewDataSource {

    @IBOutlet weak var tableView: UITableView!
    var tableViewDataSource : [Dictionary<String, String>] = [];
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        var s = "http://www.masisnguyen.com/randy/mysql_proxy.php?command=SELECTT%20*%20FROM%20"
        
        let url = URL(string: s + "UCIToday"  + "%20ORDER%20BY%20eventDate%20ASC")
        
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
            let cell = self.tableView.dequeueReusableCell(withIdentifier: "customCell", for: indexPath) as! Today_TableViewCell
            
            
            
            var dict = tableViewDataSource[indexPath.row]
            var a : String!
            a = dict["eventDate"]
            var b : String!
            if (dict["eventTime"] == "X" || dict["eventTime"] == "x") {
                b = ""
            } else {
                b = dict["eventTime"]
            }

            var c : String!
            c = dict["title"]
            var d : String!
            d = dict["location"]
            var e : String!
            e = dict["info"]

            
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
