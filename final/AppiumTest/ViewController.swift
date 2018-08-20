//
//  ViewController.swift
//  AppiumTest
//
//  Created by Lawrey on 18/8/18.
//  Copyright © 2018 Lawrey. All rights reserved.
//

import UIKit

class ViewController: UIViewController {}

extension ViewController: UITextFieldDelegate {
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        self.view.endEditing(true)
        return false
    }
}
