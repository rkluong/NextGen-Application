//
//  SportsCategories_ViewController.swift
//  NextGen
//
//  Created by Mahamadou Sylla on 3/6/17.
//  Copyright © 2017 Mahamadou Sylla. All rights reserved.
//

import UIKit

class SportsCategories_ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    // runs just before you segue to next view
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // "controller" is a reference to the view you're going to
        //let controller : Sports_ViewController = segue.destination as! Sports_ViewController
        
        if segue.identifier == "MenBball_Segue" {
            let controller : Sports_ViewController = segue.destination as! Sports_ViewController
            controller.buttonClicked = "m_baskl";
        }
        else if segue.identifier == "WomenBball_Segue" {
            let controller : Sports_ViewController = segue.destination as! Sports_ViewController
            controller.buttonClicked = "w_baskl";
        }
        else if segue.identifier == "MenBaseball_Segue" {
            let controller : Sports_ViewController = segue.destination as! Sports_ViewController
            controller.buttonClicked = "m_baseball";
        }
        else if segue.identifier == "WomenTrack_Segue" {
            let controller : Sports_ViewController = segue.destination as! Sports_ViewController
            controller.buttonClicked = "w_track";
        }
        else if segue.identifier == "Home_Segue" {
            let controller : Categories_ViewController = segue.destination as! Categories_ViewController
        }
        
//        else {
//            // this null option is if nothing was entered, meaning you encounted a problem.
//            // maybe display a error alert and segue back to view
//            //let controller : Sports_ViewController = segue.destination as! Sports_ViewController
//            controller.buttonClicked = "null";
//        }
        
    }
}
